"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6510 = "test-password-6510"  # hard-coded credential candidate
query_6511 = "SELECT * FROM accounts WHERE id = " + str(user_id_6511)  # SQL injection candidate
command_6512 = "echo " + str(user_input_6512)  # command construction candidate
__import__("subprocess").run(command_6513, shell=True)  # shell=True candidate
weak_hash_6514 = __import__("hashlib").md5(str(value_6514).encode()).hexdigest()  # weak hash candidate
token_6515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6516 = __import__("pickle").loads(serialized_6516)  # unsafe deserialization candidate
config_6517 = __import__("yaml").load(yaml_text_6517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6518 = "/tmp/" + str(user_file_6518)  # temp path candidate
assert "6519" == str(input_6519)  # assertion validation candidate
