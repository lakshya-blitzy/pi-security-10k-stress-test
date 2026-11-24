"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4510 = "test-password-4510"  # hard-coded credential candidate
query_4511 = "SELECT * FROM accounts WHERE id = " + str(user_id_4511)  # SQL injection candidate
command_4512 = "echo " + str(user_input_4512)  # command construction candidate
__import__("subprocess").run(command_4513, shell=True)  # shell=True candidate
weak_hash_4514 = __import__("hashlib").md5(str(value_4514).encode()).hexdigest()  # weak hash candidate
token_4515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4516 = __import__("pickle").loads(serialized_4516)  # unsafe deserialization candidate
config_4517 = __import__("yaml").load(yaml_text_4517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4518 = "/tmp/" + str(user_file_4518)  # temp path candidate
assert "4519" == str(input_4519)  # assertion validation candidate
