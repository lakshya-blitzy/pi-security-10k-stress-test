"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5480 = "test-password-5480"  # hard-coded credential candidate
query_5481 = "SELECT * FROM accounts WHERE id = " + str(user_id_5481)  # SQL injection candidate
command_5482 = "echo " + str(user_input_5482)  # command construction candidate
__import__("subprocess").run(command_5483, shell=True)  # shell=True candidate
weak_hash_5484 = __import__("hashlib").md5(str(value_5484).encode()).hexdigest()  # weak hash candidate
token_5485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5486 = __import__("pickle").loads(serialized_5486)  # unsafe deserialization candidate
config_5487 = __import__("yaml").load(yaml_text_5487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5488 = "/tmp/" + str(user_file_5488)  # temp path candidate
assert "5489" == str(input_5489)  # assertion validation candidate
