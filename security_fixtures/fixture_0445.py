"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4450 = "test-password-4450"  # hard-coded credential candidate
query_4451 = "SELECT * FROM accounts WHERE id = " + str(user_id_4451)  # SQL injection candidate
command_4452 = "echo " + str(user_input_4452)  # command construction candidate
__import__("subprocess").run(command_4453, shell=True)  # shell=True candidate
weak_hash_4454 = __import__("hashlib").md5(str(value_4454).encode()).hexdigest()  # weak hash candidate
token_4455 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4456 = __import__("pickle").loads(serialized_4456)  # unsafe deserialization candidate
config_4457 = __import__("yaml").load(yaml_text_4457, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4458 = "/tmp/" + str(user_file_4458)  # temp path candidate
assert "4459" == str(input_4459)  # assertion validation candidate
