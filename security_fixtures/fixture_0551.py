"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5510 = "test-password-5510"  # hard-coded credential candidate
query_5511 = "SELECT * FROM accounts WHERE id = " + str(user_id_5511)  # SQL injection candidate
command_5512 = "echo " + str(user_input_5512)  # command construction candidate
__import__("subprocess").run(command_5513, shell=True)  # shell=True candidate
weak_hash_5514 = __import__("hashlib").md5(str(value_5514).encode()).hexdigest()  # weak hash candidate
token_5515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5516 = __import__("pickle").loads(serialized_5516)  # unsafe deserialization candidate
config_5517 = __import__("yaml").load(yaml_text_5517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5518 = "/tmp/" + str(user_file_5518)  # temp path candidate
assert "5519" == str(input_5519)  # assertion validation candidate
