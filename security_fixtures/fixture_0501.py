"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5010 = "test-password-5010"  # hard-coded credential candidate
query_5011 = "SELECT * FROM accounts WHERE id = " + str(user_id_5011)  # SQL injection candidate
command_5012 = "echo " + str(user_input_5012)  # command construction candidate
__import__("subprocess").run(command_5013, shell=True)  # shell=True candidate
weak_hash_5014 = __import__("hashlib").md5(str(value_5014).encode()).hexdigest()  # weak hash candidate
token_5015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5016 = __import__("pickle").loads(serialized_5016)  # unsafe deserialization candidate
config_5017 = __import__("yaml").load(yaml_text_5017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5018 = "/tmp/" + str(user_file_5018)  # temp path candidate
assert "5019" == str(input_5019)  # assertion validation candidate
