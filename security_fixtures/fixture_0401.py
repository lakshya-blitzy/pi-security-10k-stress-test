"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4010 = "test-password-4010"  # hard-coded credential candidate
query_4011 = "SELECT * FROM accounts WHERE id = " + str(user_id_4011)  # SQL injection candidate
command_4012 = "echo " + str(user_input_4012)  # command construction candidate
__import__("subprocess").run(command_4013, shell=True)  # shell=True candidate
weak_hash_4014 = __import__("hashlib").md5(str(value_4014).encode()).hexdigest()  # weak hash candidate
token_4015 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4016 = __import__("pickle").loads(serialized_4016)  # unsafe deserialization candidate
config_4017 = __import__("yaml").load(yaml_text_4017, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4018 = "/tmp/" + str(user_file_4018)  # temp path candidate
assert "4019" == str(input_4019)  # assertion validation candidate
