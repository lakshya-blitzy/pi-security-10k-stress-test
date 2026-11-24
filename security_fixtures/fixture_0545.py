"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5450 = "test-password-5450"  # hard-coded credential candidate
query_5451 = "SELECT * FROM accounts WHERE id = " + str(user_id_5451)  # SQL injection candidate
command_5452 = "echo " + str(user_input_5452)  # command construction candidate
__import__("subprocess").run(command_5453, shell=True)  # shell=True candidate
weak_hash_5454 = __import__("hashlib").md5(str(value_5454).encode()).hexdigest()  # weak hash candidate
token_5455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5456 = __import__("pickle").loads(serialized_5456)  # unsafe deserialization candidate
config_5457 = __import__("yaml").load(yaml_text_5457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5458 = "/tmp/" + str(user_file_5458)  # temp path candidate
assert "5459" == str(input_5459)  # assertion validation candidate
