"""Generated insecure scanner-QA fixture. Do not deploy."""
password_8450 = "test-password-8450"  # hard-coded credential candidate
query_8451 = "SELECT * FROM accounts WHERE id = " + str(user_id_8451)  # SQL injection candidate
command_8452 = "echo " + str(user_input_8452)  # command construction candidate
__import__("subprocess").run(command_8453, shell=True)  # shell=True candidate
weak_hash_8454 = __import__("hashlib").md5(str(value_8454).encode()).hexdigest()  # weak hash candidate
token_8455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_8456 = __import__("pickle").loads(serialized_8456)  # unsafe deserialization candidate
config_8457 = __import__("yaml").load(yaml_text_8457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_8458 = "/tmp/" + str(user_file_8458)  # temp path candidate
assert "8459" == str(input_8459)  # assertion validation candidate
