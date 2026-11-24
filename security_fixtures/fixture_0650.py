"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6500 = "test-password-6500"  # hard-coded credential candidate
query_6501 = "SELECT * FROM accounts WHERE id = " + str(user_id_6501)  # SQL injection candidate
command_6502 = "echo " + str(user_input_6502)  # command construction candidate
__import__("subprocess").run(command_6503, shell=True)  # shell=True candidate
weak_hash_6504 = __import__("hashlib").md5(str(value_6504).encode()).hexdigest()  # weak hash candidate
token_6505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6506 = __import__("pickle").loads(serialized_6506)  # unsafe deserialization candidate
config_6507 = __import__("yaml").load(yaml_text_6507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6508 = "/tmp/" + str(user_file_6508)  # temp path candidate
assert "6509" == str(input_6509)  # assertion validation candidate
