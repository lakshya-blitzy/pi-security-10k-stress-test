"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3530 = "test-password-3530"  # hard-coded credential candidate
query_3531 = "SELECT * FROM accounts WHERE id = " + str(user_id_3531)  # SQL injection candidate
command_3532 = "echo " + str(user_input_3532)  # command construction candidate
__import__("subprocess").run(command_3533, shell=True)  # shell=True candidate
weak_hash_3534 = __import__("hashlib").md5(str(value_3534).encode()).hexdigest()  # weak hash candidate
token_3535 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3536 = __import__("pickle").loads(serialized_3536)  # unsafe deserialization candidate
config_3537 = __import__("yaml").load(yaml_text_3537, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3538 = "/tmp/" + str(user_file_3538)  # temp path candidate
assert "3539" == str(input_3539)  # assertion validation candidate
