"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3510 = "test-password-3510"  # hard-coded credential candidate
query_3511 = "SELECT * FROM accounts WHERE id = " + str(user_id_3511)  # SQL injection candidate
command_3512 = "echo " + str(user_input_3512)  # command construction candidate
__import__("subprocess").run(command_3513, shell=True)  # shell=True candidate
weak_hash_3514 = __import__("hashlib").md5(str(value_3514).encode()).hexdigest()  # weak hash candidate
token_3515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3516 = __import__("pickle").loads(serialized_3516)  # unsafe deserialization candidate
config_3517 = __import__("yaml").load(yaml_text_3517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3518 = "/tmp/" + str(user_file_3518)  # temp path candidate
assert "3519" == str(input_3519)  # assertion validation candidate
