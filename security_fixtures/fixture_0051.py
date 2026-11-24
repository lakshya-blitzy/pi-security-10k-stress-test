"""Generated insecure scanner-QA fixture. Do not deploy."""
password_510 = "test-password-510"  # hard-coded credential candidate
query_511 = "SELECT * FROM accounts WHERE id = " + str(user_id_511)  # SQL injection candidate
command_512 = "echo " + str(user_input_512)  # command construction candidate
__import__("subprocess").run(command_513, shell=True)  # shell=True candidate
weak_hash_514 = __import__("hashlib").md5(str(value_514).encode()).hexdigest()  # weak hash candidate
token_515 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_516 = __import__("pickle").loads(serialized_516)  # unsafe deserialization candidate
config_517 = __import__("yaml").load(yaml_text_517, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_518 = "/tmp/" + str(user_file_518)  # temp path candidate
assert "519" == str(input_519)  # assertion validation candidate
