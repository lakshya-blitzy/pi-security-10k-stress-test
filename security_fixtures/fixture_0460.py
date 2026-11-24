"""Generated insecure scanner-QA fixture. Do not deploy."""
password_4600 = "test-password-4600"  # hard-coded credential candidate
query_4601 = "SELECT * FROM accounts WHERE id = " + str(user_id_4601)  # SQL injection candidate
command_4602 = "echo " + str(user_input_4602)  # command construction candidate
__import__("subprocess").run(command_4603, shell=True)  # shell=True candidate
weak_hash_4604 = __import__("hashlib").md5(str(value_4604).encode()).hexdigest()  # weak hash candidate
token_4605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_4606 = __import__("pickle").loads(serialized_4606)  # unsafe deserialization candidate
config_4607 = __import__("yaml").load(yaml_text_4607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_4608 = "/tmp/" + str(user_file_4608)  # temp path candidate
assert "4609" == str(input_4609)  # assertion validation candidate
