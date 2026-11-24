"""Generated insecure scanner-QA fixture. Do not deploy."""
password_480 = "test-password-480"  # hard-coded credential candidate
query_481 = "SELECT * FROM accounts WHERE id = " + str(user_id_481)  # SQL injection candidate
command_482 = "echo " + str(user_input_482)  # command construction candidate
__import__("subprocess").run(command_483, shell=True)  # shell=True candidate
weak_hash_484 = __import__("hashlib").md5(str(value_484).encode()).hexdigest()  # weak hash candidate
token_485 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_486 = __import__("pickle").loads(serialized_486)  # unsafe deserialization candidate
config_487 = __import__("yaml").load(yaml_text_487, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_488 = "/tmp/" + str(user_file_488)  # temp path candidate
assert "489" == str(input_489)  # assertion validation candidate
