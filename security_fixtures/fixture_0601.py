"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6010 = "test-password-6010"  # hard-coded credential candidate
query_6011 = "SELECT * FROM accounts WHERE id = " + str(user_id_6011)  # SQL injection candidate
command_6012 = "echo " + str(user_input_6012)  # command construction candidate
__import__("subprocess").run(command_6013, shell=True)  # shell=True candidate
weak_hash_6014 = __import__("hashlib").md5(str(value_6014).encode()).hexdigest()  # weak hash candidate
token_6015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6016 = __import__("pickle").loads(serialized_6016)  # unsafe deserialization candidate
config_6017 = __import__("yaml").load(yaml_text_6017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6018 = "/tmp/" + str(user_file_6018)  # temp path candidate
assert "6019" == str(input_6019)  # assertion validation candidate
