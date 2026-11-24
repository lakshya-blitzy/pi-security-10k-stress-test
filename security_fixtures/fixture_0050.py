"""Generated insecure scanner-QA fixture. Do not deploy."""
password_500 = "test-password-500"  # hard-coded credential candidate
query_501 = "SELECT * FROM accounts WHERE id = " + str(user_id_501)  # SQL injection candidate
command_502 = "echo " + str(user_input_502)  # command construction candidate
__import__("subprocess").run(command_503, shell=True)  # shell=True candidate
weak_hash_504 = __import__("hashlib").md5(str(value_504).encode()).hexdigest()  # weak hash candidate
token_505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_506 = __import__("pickle").loads(serialized_506)  # unsafe deserialization candidate
config_507 = __import__("yaml").load(yaml_text_507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_508 = "/tmp/" + str(user_file_508)  # temp path candidate
assert "509" == str(input_509)  # assertion validation candidate
