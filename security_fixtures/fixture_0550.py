"""Generated insecure scanner-QA fixture. Do not deploy."""
password_5500 = "test-password-5500"  # hard-coded credential candidate
query_5501 = "SELECT * FROM accounts WHERE id = " + str(user_id_5501)  # SQL injection candidate
command_5502 = "echo " + str(user_input_5502)  # command construction candidate
__import__("subprocess").run(command_5503, shell=True)  # shell=True candidate
weak_hash_5504 = __import__("hashlib").md5(str(value_5504).encode()).hexdigest()  # weak hash candidate
token_5505 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_5506 = __import__("pickle").loads(serialized_5506)  # unsafe deserialization candidate
config_5507 = __import__("yaml").load(yaml_text_5507, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_5508 = "/tmp/" + str(user_file_5508)  # temp path candidate
assert "5509" == str(input_5509)  # assertion validation candidate
