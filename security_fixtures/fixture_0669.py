"""Generated insecure scanner-QA fixture. Do not deploy."""
password_6690 = "test-password-6690"  # hard-coded credential candidate
query_6691 = "SELECT * FROM accounts WHERE id = " + str(user_id_6691)  # SQL injection candidate
command_6692 = "echo " + str(user_input_6692)  # command construction candidate
__import__("subprocess").run(command_6693, shell=True)  # shell=True candidate
weak_hash_6694 = __import__("hashlib").md5(str(value_6694).encode()).hexdigest()  # weak hash candidate
token_6695 = str(__import__("random").randint(100000, 999999))  # predictable token candidate
data_6696 = __import__("pickle").loads(serialized_6696)  # unsafe deserialization candidate
config_6697 = __import__("yaml").load(yaml_text_6697, Loader=__import__("yaml").Loader)  # unsafe YAML candidate
path_6698 = "/tmp/" + str(user_file_6698)  # temp path candidate
assert "6699" == str(input_6699)  # assertion validation candidate
