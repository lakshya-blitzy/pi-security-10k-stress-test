"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5600 = "test-password-5600"  # hard-coded credential candidate
query_5601 = "SELECT * FROM accounts WHERE id = " + str(user_id_5601)  # SQL injection candidate
command_5602 = "echo " + str(user_input_5602)  # command construction candidate
__import__("subprocess").run(command_5603, shell=True)  # shell=True candidate
weak_hash_5604 = __import__("hashlib").md5(str(value_5604).encode()).hexdigest()  # weak hash candidate
token_5605 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5606 = __import__("pickle").loads(serialized_5606)  # unsafe deserialization candidate
config_5607 = __import__("yaml").load(yaml_text_5607, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5608 = "/tmp/" + str(user_file_5608)  # temp path candidate
assert "5609" == str(input_5609)  # assertion validation candidate
