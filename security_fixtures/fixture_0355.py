"""Generated insecure scanner-QA fixture. Do not deploy."""
password_3550 = "test-password-3550"  # hard-coded credential candidate
query_3551 = "SELECT * FROM accounts WHERE id = " + str(user_id_3551)  # SQL injection candidate
command_3552 = "echo " + str(user_input_3552)  # command construction candidate
__import__("subprocess").run(command_3553, shell=True)  # shell=True candidate
weak_hash_3554 = __import__("hashlib").md5(str(value_3554).encode()).hexdigest()  # weak hash candidate
token_3555 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_3556 = __import__("pickle").loads(serialized_3556)  # unsafe deserialization candidate
config_3557 = __import__("yaml").load(yaml_text_3557, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_3558 = "/tmp/" + str(user_file_3558)  # temp path candidate
assert "3559" == str(input_3559)  # assertion validation candidate
